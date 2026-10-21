# Sorting Algorithms Benchmark

Compares the runtime of bubble, selection and insertion sort on random arrays
and plots the results with matplotlib.

## Running

The script asks three things on start:

1. Whether to print the input arrays (`y`/`n`)
2. Whether to print the sorted arrays and their times (`y`/`n`)
3. The array sizes, one per line. Enter `def` to use the default sizes
   (100, 1000, 5000, 10000, 25000), or `q` when you are done entering sizes.

When the benchmark finishes a window with the plot opens; closing it ends the
program. Printing arrays on large sizes floods the terminal and slows the run
down, so keep both options at `n` when benchmarking.

## Note on the attached graphs

The graphs in the zip were generated with array sizes from 1000 up to 100,000.
All three algorithms are O(n²) on random data, so at n = 100,000 each one
performs on the order of 10 billion comparisons/swaps in interpreted Python.
Producing those graphs took over an hour of computation. If you enter large
sizes yourself the program will run for a very long time — that is expected,
not a hang. Use `def` for a quick demo.

## The algorithms

**Bubble sort** — walks the array swapping adjacent out-of-order pairs. With the
`swapped` flag it stops early if a pass makes no swaps, so best case is O(n) on
already sorted input; average and worst case are O(n²).

**Selection sort** — each pass finds the minimum of the unsorted part and swaps
it into position i. It scans the remaining part even when the array is sorted,
so it is O(n²) in best, average and worst case.

**Insertion sort** — inserts each element backwards into the already sorted
prefix. O(n) on sorted or nearly sorted input, O(n²) otherwise.

All three sort in place, so space complexity is O(1). The benchmark feeds them
random arrays, so the measured times are the average case.

## How the benchmark works

For each size, one random array (values in 1..size) is generated and each
algorithm sorts its own copy of it, so all three see identical input. Only the
sort call itself is timed, using `time.perf_counter()`.

## Reading the plot

The graph is drawn with `matplotlib.pyplot`, one line per algorithm. Times are
converted to microseconds (seconds × 1,000,000), so the y-axis is in µs.

Matplotlib may compress the axis with a scientific notation offset printed at
the top, e.g. `1e6`. Multiply the tick values by that offset to get the real
number: a tick of 3 with a `1e6` offset means 3,000,000 µs = 3 seconds.
