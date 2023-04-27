# CS230-Project
# Cache Hierarchy Optimization for Graph Analytics

# Inclusive folder contains the implementation of Inclusive hierarchy


build using ./build_champsim.sh ${BRANCH} ${L1I_PREFETCHER} ${L1D_PREFETCHER} ${L2C_PREFETCHER} ${LLC_PREFETCHER} ${LLC_REPLACEMENT} ${NUM_CORE} in inclusive folder 
run for a single core using ./run_champsim.sh [BINARY] [N_WARM] [N_SIM] [TRACE] [OPTION] in inclusive folder
for multicore simulation use ./run_4core.sh [BINARY] [N_WARM] [N_SIM] [N_MIX] [TRACE0] [TRACE1] [TRACE2] [TRACE3] [OPTION] in inclusive folder

# Non Inclusive folder contains the implementation of Non Inclusive hierarchy

build using ./build_champsim.sh ${BRANCH} ${L1I_PREFETCHER} ${L1D_PREFETCHER} ${L2C_PREFETCHER} ${LLC_PREFETCHER} ${LLC_REPLACEMENT} ${NUM_CORE} in non inclusive folder
run for a single core using ./run_champsim.sh [BINARY] [N_WARM] [N_SIM] [TRACE] [OPTION] in non inclusive folder
for multicore simulation use ./run_4core.sh [BINARY] [N_WARM] [N_SIM] [N_MIX] [TRACE0] [TRACE1] [TRACE2] [TRACE3] [OPTION] in non inclusive folder


# Exclusive folder contains the implementation of Exclusive hierarchy

build using ./build_champsim.sh ${BRANCH} ${L1I_PREFETCHER} ${L1D_PREFETCHER} ${L2C_PREFETCHER} ${LLC_PREFETCHER} ${LLC_REPLACEMENT} ${NUM_CORE} in exclusive folder
run for a single core using ./run_champsim.sh [BINARY] [N_WARM] [N_SIM] [TRACE] [OPTION] in exclusive folder
for multicore simulation use ./run_4core.sh [BINARY] [N_WARM] [N_SIM] [N_MIX] [TRACE0] [TRACE1] [TRACE2] [TRACE3] [OPTION] in exclusive folder
 
# References
https://par.nsf.gov/servlets/purl/10080635
https://core.ac.uk/download/pdf/147122148.pdf

# Slides
https://docs.google.com/presentation/d/1XqtdgzVV2iu7CNtL7bDkFWFopBfgSn-c0ZYugHMx-0g/edit?usp=sharing

# Video link
https://drive.google.com/file/d/1Px4bvy9hA_yisp8Zanvp_LfXM-CuSYMA/view?usp=share_link
