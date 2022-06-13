# REPORT

## Personal Information
- Student Name: Kunyang
- Student ID: 20958936
- WatID: k47xie

## What have been done to compile and run the code

Firstly installed the Docker, which provides the running environment, then I downloaded the doom image.

In the docker environment, I run several commands as follow:

```bash
git clone https://git.uwaterloo.ca/stqam-1225/class/k47xie.git stqam
cd stqam/fb
git clone https://git.uwaterloo.ca/stqam-1225/chocolate-doom.git
mkdir build
cd build
cmake -DCMAKE_C_COMPILER=clang-10 -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
	-DCMAKE_C_FLAGS='-fsanitize=fuzzer-no-link,address -fprofile-instr-generate -fcoverage-mapping -g -ggdb3 -O2' \ 
	../ -GNinja
ninja
export ASAN_OPTIONS=detect_leaks=0 
export LLVM_PROFILE_FILE='pf-%p' 
./src/doom_fuzz -runs=10  CORPUS SEED -jobs=100 -workers=8 -detect_leaks=0 >/dev/null
ls pf-* > all_prof_files
llvm-profdata-10 merge -sparse -f all_prof_files -o default.profdata
llvm-cov-10 export ./src/doom_fuzz -instr-profile=default.profdata -format=lcov > src.info
lcov -a src.info -o src_report.info
genhtml -o html_output src_report.info
```

Finally, we have the coverage report. 

## What have been done to increase the coverage

Added `hershcel.wad` to the SEED folder, then created testing cases.

## What bugs have been found? Can you replay the bug with chocolate-doom, not with the fuzz target?

```bash
AddressSanitizer:DEADLYSIGNAL
=================================================================
==64427==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000070 (pc 0x000000574ac5 bp 0x7ffc39157ff0 sp 0x7ffc39157ec0 T0)
==64427==The signal is caused by a WRITE memory access.
==64427==Hint: address points to the zero page.
    #0 0x574ac5 in P_GroupLines /home/doom/k47xie/fb/build/../chocolate-doom/src/doom/p_setup.c:593:28
    #1 0x575ed7 in P_SetupLevel /home/doom/k47xie/fb/build/../chocolate-doom/src/doom/p_setup.c:838:5
    #2 0x4ff201 in G_DoLoadLevel /home/doom/k47xie/fb/build/../chocolate-doom/src/doom/g_game.c:657:5
    #3 0x478419 in LLVMFuzzerTestOneInput /home/doom/k47xie/fb/build/../src/fuzz_target.c:271:3
    #4 0x382a51 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/k47xie/fb/build/src/doom_fuzz+0x382a51)
    #5 0x382195 in fuzzer::Fuzzer::RunOne(unsigned char const*, unsigned long, bool, fuzzer::InputInfo*, bool*) (/home/doom/k47xie/fb/build/src/doom_fuzz+0x382195)
    #6 0x384ab7 in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/k47xie/fb/build/src/doom_fuzz+0x384ab7)
    #7 0x384e19 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/k47xie/fb/build/src/doom_fuzz+0x384e19)
    #8 0x372e9e in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/k47xie/fb/build/src/doom_fuzz+0x372e9e)
    #9 0x39c932 in main (/home/doom/k47xie/fb/build/src/doom_fuzz+0x39c932)
    #10 0x7f839ca76bf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)
    #11 0x347c19 in _start (/home/doom/k47xie/fb/build/src/doom_fuzz+0x347c19)
```

## Did you manage to compile the game and play it on your local machine (Not inside Docker)?

Yes
