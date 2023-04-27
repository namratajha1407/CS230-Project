# Cache Hierarchy Optimization for Graph Analytics

Before moving further, create a directory inside the inclusive/non_inclusive/exclusive folder name dpc3_traces and add your trace there.

## Inclusive folder contains the implementation of Inclusive hierarchy

build using 
'''./build_champsim.sh ${BRANCH} ${L1I_PREFETCHER} ${L1D_PREFETCHER} ${L2C_PREFETCHER} ${LLC_PREFETCHER} ${LLC_REPLACEMENT} ${NUM_CORE}''' in inclusive folder  <br>
run for a single core using ./run_champsim.sh [BINARY] [N_WARM] [N_SIM] [TRACE] [OPTION] in inclusive folder  <br>
for multicore simulation use ./run_4core.sh [BINARY] [N_WARM] [N_SIM] [N_MIX] [TRACE0] [TRACE1] [TRACE2] [TRACE3] [OPTION] in inclusive folder  <br>

## Non Inclusive folder contains the implementation of Non Inclusive hierarchy

build using ./build_champsim.sh ${BRANCH} ${L1I_PREFETCHER} ${L1D_PREFETCHER} ${L2C_PREFETCHER} ${LLC_PREFETCHER} ${LLC_REPLACEMENT} ${NUM_CORE} in non inclusive folder  <br>
run for a single core using ./run_champsim.sh [BINARY] [N_WARM] [N_SIM] [TRACE] [OPTION] in non inclusive folder  <br>
for multicore simulation use ./run_4core.sh [BINARY] [N_WARM] [N_SIM] [N_MIX] [TRACE0] [TRACE1] [TRACE2] [TRACE3] [OPTION] in non inclusive folder  <br>


## Exclusive folder contains the implementation of Exclusive hierarchy

build using ./build_champsim.sh ${BRANCH} ${L1I_PREFETCHER} ${L1D_PREFETCHER} ${L2C_PREFETCHER} ${LLC_PREFETCHER} ${LLC_REPLACEMENT} ${NUM_CORE} in exclusive folder  <br>
run for a single core using ./run_champsim.sh [BINARY] [N_WARM] [N_SIM] [TRACE] [OPTION] in exclusive folder  <br>
for multicore simulation use ./run_4core.sh [BINARY] [N_WARM] [N_SIM] [N_MIX] [TRACE0] [TRACE1] [TRACE2] [TRACE3] [OPTION] in exclusive folder  <br>
 
## References
https://par.nsf.gov/servlets/purl/10080635  <br>
https://core.ac.uk/download/pdf/147122148.pdf

## Slides
https://docs.google.com/presentation/d/1XqtdgzVV2iu7CNtL7bDkFWFopBfgSn-c0ZYugHMx-0g/edit?usp=sharing

## Video link
https://drive.google.com/file/d/1Px4bvy9hA_yisp8Zanvp_LfXM-CuSYMA/view?usp=share_link
