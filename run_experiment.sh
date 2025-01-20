#!/bin/bash
seed=10 # change the seed if you want to
filename="seed${seed}"
mkdir "${filename}"
cd "${filename}"

# Configure Git to increase buffer size
git config --global http.postBuffer 524288000
git config --global http.maxRequestBuffer 1048576000

# git clone https://github.com/zbh888/LEOhandover.git main
git clone https://github.com/saharraisi/LEOhandover.git main

# input_array=(10000 20000 30000 40000 50000 60000 70000) # Modify this array with your desired values
input_array=(10000 20000)

for value in "${input_array[@]}"; do
    cp -r main "main${value}"
    cd "main${value}"
    sed -i "2s/.*/SEED = $seed/" ./src/config.py
    sed -i "3s/.*/NUMBER_UE = $value/" ./src/config.py
    cd ..
done

git config --global http.postBuffer 524288000
git config --global http.maxRequestBuffer 1048576000

# git clone -b group https://github.com/zbh888/LEOhandover.git group
git clone -b group https://github.com/saharraisi/LEOhandover.git group

for value in "${input_array[@]}"; do
    cp -r group "group${value}"
    cd "group${value}"
    sed -i "2s/.*/SEED = $seed/" ./src/config.py
    sed -i "3s/.*/NUMBER_UE = $value/" ./src/config.py
    cd ..
done

# rm -rf main group

for value in "${input_array[@]}"; do
    cd "group${value}"
    ./default_run.sh
    cd ..
    
    cd "main${value}"
    ./default_run.sh
    cd ..
done

# for value in "${input_array[@]}"; do
#     cd "group${value}"
#     nohup ./default_run.sh &
#     cd ..
#     cd "main${value}"
#     nohup ./default_run.sh &
#     cd ..
# done


#!/bin/bash
# seed=10 # change the seed if you want to
# filename="seed${seed}"
# mkdir "${filename}"
# cd "${filename}"

# git clone https://github.com/zbh888/LEOhandover.git main

# input_array=(10000 20000 30000 40000 50000 60000 70000) # Modify this array with your desired values

# for value in "${input_array[@]}"; do
#     cp -r main "main${value}"
#     cd "main${value}"
#     sed -i "2s/.*/SEED = $seed/" ./src/config.py
#     sed -i "3s/.*/NUMBER_UE = $value/" ./src/config.py
#     cd ..
# done

# git clone -b group https://github.com/zbh888/LEOhandover.git group

# for value in "${input_array[@]}"; do
#     cp -r group "group${value}"
#     cd "group${value}"
#     sed -i "2s/.*/SEED = $seed/" ./src/config.py
#     sed -i "3s/.*/NUMBER_UE = $value/" ./src/config.py
#     cd ..
# done

# rm -rf main group


# for value in "${input_array[@]}"; do
#     cd "group${value}"
#     nohup ./default_run.sh &
#     cd ..
#     cd "main${value}"
#     nohup ./default_run.sh &
#     cd ..
# done



