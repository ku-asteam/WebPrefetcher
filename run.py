# Import
import json
import os
import subprocess

# Experimental variables
LOG_TAG = "run.py"
SCENARIO_DIR = "./scenario/"
SCENARIO_FILE = "top3_scenario.json"
BRIDGE_ENABLED = True

# Set up Docker networks for throttling
if BRIDGE_ENABLED == True:
    print("[{0:s}] Starting Docker networks".format(LOG_TAG))

    subprocess.run("sudo docker network create --driver bridge --subnet=192.168.34.0/24 --gateway=192.168.34.10 --opt \"com.docker.network.bridge.name\"=\"docker1\" cable", shell=True, check=True)
    subprocess.run("sudo tc qdisc add dev docker1 root handle 1: htb default 12", shell=True, check=True)
    subprocess.run("sudo tc class add dev docker1 parent 1:1 classid 1:12 htb rate 5mbit ceil 5mbit", shell=True, check=True)
    subprocess.run("sudo tc qdisc add dev docker1 parent 1:12 netem delay 14ms", shell=True, check=True)
 
    subprocess.run("sudo docker network create --driver bridge --subnet=192.168.33.0/24 --gateway=192.168.33.10 --opt \"com.docker.network.bridge.name\"=\"docker2\" 3g", shell=True, check=True)
    subprocess.run("sudo tc qdisc add dev docker2 root handle 1: htb default 12", shell=True, check=True)
    subprocess.run("sudo tc class add dev docker2 parent 1:1 classid 1:12 htb rate 1.6mbit ceil 1.6mbit", shell=True, check=True)
    subprocess.run("sudo tc qdisc add dev docker2 parent 1:12 netem delay 150ms", shell=True, check=True)    

    subprocess.run("sudo docker network create --driver bridge --subnet=192.168.35.0/24 --gateway=192.168.35.10 --opt \"com.docker.network.bridge.name\"=\"docker3\" 3gfast", shell=True, check=True)
    subprocess.run("sudo tc qdisc add dev docker3 root handle 1: htb default 12", shell=True, check=True)
    subprocess.run("sudo tc class add dev docker3 parent 1:1 classid 1:12 htb rate 1.6mbit ceil 1.6mbit", shell=True, check=True)
    subprocess.run("sudo tc qdisc add dev docker3 parent 1:12 netem delay 75ms", shell=True, check=True)

    subprocess.run("sudo docker network create --driver bridge --subnet=192.168.36.0/24 --gateway=192.168.36.10 --opt \"com.docker.network.bridge.name\"=\"docker4\" 3gslow", shell=True, check=True)
    subprocess.run("sudo tc qdisc add dev docker4 root handle 1: htb default 12", shell=True, check=True)
    subprocess.run("sudo tc class add dev docker4 parent 1:1 classid 1:12 htb rate 0.4mbit ceil 0.4mbit", shell=True, check=True)
    subprocess.run("sudo tc qdisc add dev docker4 parent 1:12 netem delay 200ms", shell=True, check=True)

    #print("[{0:s}] After starting:".format("docker"))
    #subprocess.run("sudo docker network ls", shell=True, check=True)
else:
    print("[{0:s}] Docker networks disabled".format(LOG_TAG))

# Load scenarios
SCENARIO_PATH = os.path.join(SCENARIO_DIR, SCENARIO_FILE)
f = open(SCENARIO_PATH, 'r', encoding='UTF8')
scenario_json = json.loads(f.read())
f.close()
print("[{0:s}] Scenario file loaded: {1:s}".format(LOG_TAG, SCENARIO_PATH))
print("[{0:s}]  - top_k: {1:d}".format(LOG_TAG, scenario_json["top_k"]))
print("[{0:s}]  - n_scenario: {1:d}".format(LOG_TAG, scenario_json["n_scenario"]))
print("[{0:s}]  - test_precition: {1:f}".format(LOG_TAG, scenario_json["test_precition"]))
print("[{0:s}]  - test_recall: {1:f}".format(LOG_TAG, scenario_json["test_recall"]))
print("[{0:s}]  - test_f-measure: {1:f}".format(LOG_TAG, scenario_json["test_f-measure"]))

# Run browsertime
profile_list = ["cable"]  # cable, 3gfast, 3g, 3gslow
prefetch_list = ["prefetch"]    # none, prefetch, complete, prefetch_correct

for profile in profile_list:
    #################### EACH NETWORK PROFILE ####################
    net_opt = "bridge"                                  # --network=
    con_opt = "native"                                  # -c
    if BRIDGE_ENABLED == True:
        net_opt = profile
        con_opt = profile
    add_timer = "true"                                  # true, false
    page_load_strategy = "none"                         # none, eager, normal
    browser = "chrome"                                  # chrome, firefox, safari
    iter_opt = 3                                        # -n
    view_port = "1920x1080"                             # WIDTHxHEIGHT, maximize
    pre_script = "pre.js"                               # --preScript
    output_file = "output"                              # followed by '.json'; default: browsertime.json
    
    for idx in range(len(scenario_json["scenarios"])) :
        #################### EACH SCENARIO ####################
        print("[{0:s}] ********* ({1:s}, {2:d}/{3:d}) - Start *********".format(LOG_TAG, profile, idx + 1, len(scenario_json["scenarios"])))

        for prefetch_type in prefetch_list :
        #################### EACH PREFETCH ####################
            print("[{0:s}] ********* ({1:s}, {2:s}) - Start *********".format(LOG_TAG, profile, prefetch_type))

            result_dir = "./output/{0:s}_{1:s}_{2:s}_{3:d}".format(SCENARIO_FILE.split("_")[0], profile, prefetch_type, idx)
            scenario = scenario_json["scenarios"][idx]
            scenario["type"] = prefetch_type                                # none, prefetch, complete
            my_param = json.dumps(scenario, sort_keys=True, indent=None)    # additional parameters for the prescript
            url = scenario["answer_url"]

            browsertime_command = "sudo docker run --shm-size=1g --network={0:s} --rm -v \"$(pwd)\":/browsertime sitespeedio/browsertime:latest -c {1:s} --videoParams.addTimer {2:s} --pageLoadStrategy {3:s} --video --visualMetrics --prettyPrint -b {4:s} -n {5:d} --viewPort {6:s} --preScript {7:s} -o {8:s} --resultDir {9:s} --my.param '{10:s}' {11:s}".format(net_opt, con_opt, add_timer, page_load_strategy, browser, iter_opt, view_port, pre_script, output_file, result_dir, my_param, url)
            subprocess.run(browsertime_command, shell=True, check=False)
            #################### EACH PREFETCH ####################
        
        print("[{0:s}] ********* ({1:s}, {2:d}/{3:d}) - End *********".format(LOG_TAG, profile, idx + 1, len(scenario_json["scenarios"])))
        #################### EACH SCENARIO ####################

    #################### EACH NETWORK PROFILE ####################

# Clear Docker networks if set up
if BRIDGE_ENABLED == True:
    print("[{0:s}] Stopping Docker networks".format(LOG_TAG))
    
    subprocess.run("sudo docker network rm cable", shell=True, check=True)
    subprocess.run("sudo docker network rm 3g", shell=True, check=True)
    subprocess.run("sudo docker network rm 3gfast", shell=True, check=True)
    subprocess.run("sudo docker network rm 3gslow", shell=True, check=True)

    #print("[{0:s}] After stopping:".format("docker"))
    #subprocess.run("sudo docker network ls", shell=True, check=True)
