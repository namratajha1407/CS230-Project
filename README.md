# Cache Hierarchy Optimization for Graph Analytics

Before moving further, create a directory inside the inclusive/non_inclusive/exclusive folder name **dpc3_traces** and add your trace there.

## Inclusive folder contains the implementation of Inclusive hierarchy

build in inclusive folder using 
```bash
./build_champsim.sh ${BRANCH} ${L1I_PREFETCHER} ${L1D_PREFETCHER} ${L2C_PREFETCHER} ${LLC_PREFETCHER} ${LLC_REPLACEMENT} ${NUM_CORE}
```

## Non Inclusive folder contains the implementation of Non Inclusive hierarchy

build in non inclusive folder using 
```
./build_champsim.sh ${BRANCH} ${L1I_PREFETCHER} ${L1D_PREFETCHER} ${L2C_PREFETCHER} ${LLC_PREFETCHER} ${LLC_REPLACEMENT} ${NUM_CORE}
```

## Exclusive folder contains the implementation of Exclusive hierarchy

build in exclusive folder using 
```
./build_champsim.sh ${BRANCH} ${L1I_PREFETCHER} ${L1D_PREFETCHER} ${L2C_PREFETCHER} ${LLC_PREFETCHER} ${LLC_REPLACEMENT} ${NUM_CORE}
```

## Running the code
run for a single core in the respective folder using 
```
./run_champsim.sh [BINARY] [N_WARM] [N_SIM] [TRACE] [OPTION]
```
for multicore simulation in the respective folder use 
```
./run_4core.sh [BINARY] [N_WARM] [N_SIM] [N_MIX] [TRACE0] [TRACE1] [TRACE2] [TRACE3] [OPTION]
```
## References
https://par.nsf.gov/servlets/purl/10080635  <br>
https://core.ac.uk/download/pdf/147122148.pdf

## Slides
https://docs.google.com/presentation/d/1XqtdgzVV2iu7CNtL7bDkFWFopBfgSn-c0ZYugHMx-0g/edit?usp=sharing

## Video link
https://drive.google.com/file/d/1Px4bvy9hA_yisp8Zanvp_LfXM-CuSYMA/view?usp=share_link
