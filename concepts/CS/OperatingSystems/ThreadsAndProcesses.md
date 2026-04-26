# Threads and Processes
> A thread in computing systems is the smallest unit of execution that can be schduled by the OS, with it's own control flow but with some shared resources within it's parent program. Thread has it's own stack, instruction pointer, registers but also has shared heap memory, open files, OS resources within it's parent process.  

> While a process is an container of execution that operating system uses to manage and organize multiple programs(sequence of instructions), a single process can have multiple threads running within it, but at least one thread of execution is running. A process allows isolation, resource ownership and security boundary.

# Concurrency and Parallelism
These are techniques and methods used by computing systems to make the most out of the hardware's capabilities. That is using the CPU at it's maximum capacity without having any idle time and not wasting CPU cycles in waiting.
## Concurrency
Concurrency is when two or more processes are executed simultaneously but by switching context between them again and again. That is there is interleaving of processes, at one unit of time only one process is making progress. But the OS switches between processes very rapidly, so it gives the impression that all processes are making progress together. This is where scheduling algorithms come into play. Round robin, shortest job first, LIFO, FIFO etc.

## Parallelism
Parallelism is when two or more processes/threads are working simulataneously and making progress together at the same moment of time. There is no interleaving, two different CPU's are working at the same time. This can be made possible by multicore processors, multi cpu configuration or distributed systems(multiple computers working at the same time).

## Issues and Cautions with Concurrency and Parallelism
- Processes need to be synchronized.
- Deadlocks, starvation, race conditions
- resource leakage, zombie processes, threads, cleanup.
- memory corruption can happen
