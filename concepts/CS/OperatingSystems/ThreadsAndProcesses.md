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
- memory corruption can happen.
- Code is difficult to understand and is also difficult to debug.

## How to decide which concurrency model to use?
- Check for cpu bound vs I/O bound processing
- Check for blocking and non blocking I/O
- Check for memory and CPU usage constraints
- Use asyncio for non blocking I/O which internally uses event loop and yielding functions(generators). Also known as coroutines.
- Use threads when blocking I/O and isolation is required.
- Use processes when cpu bound and strong isolation is required and parallellization of tasks is possible.
- Use combination of processes and asyncio for optimal usage of resources.

## Threads in detail
- A thread is the smallest unit of execution that can be scheduled by the OS. 
- A single program/process has at least one thread of execution called main thread. 
- There can be many threads executing in a single program. They can be running parallel on different CPU cores and also they can be running concurrently using time slicing/interleaving of threads.
- Threads are useful when we want to make most of our CPU time. We use threads when we need concurrent programming like one thread for UI and other for processing the user input. So, the user interface is interactive and not stuck and lagging. 
- Also they can be used when we can parallelize our work, that is we can solve two parts of the problem independently in different threads. 
- Threads in python are generally not truly parallel they are concurrently executing.