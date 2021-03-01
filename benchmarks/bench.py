import subprocess

def eslint_bench(project):
    project = "projects/" + project
    subprocess.run([
        "npm",
        "run",
        "eslint",
        "--",
        "--no-eslintrc",
        "--ext",
        ".js",
        "--ext",
        ".ts",
        project,
    ], cwd="./benchmarks")

def rslint_bench(project):
    project = "projects/" + project
    subprocess.run([ "../target/release/rslint", project ], cwd="./benchmarks")

def test_eslint_oak(benchmark):
    benchmark(eslint_bench, "oak")

def test_rslint_oak(benchmark):
    benchmark(rslint_bench, "oak")

def test_eslint_engine262(benchmark):
    benchmark(eslint_bench, "engine262")

def test_rslint_engine262(benchmark):
    benchmark(rslint_bench, "engine262")
