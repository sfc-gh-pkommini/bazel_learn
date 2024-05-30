# bazel_learn

Repo for learning bazel with python.

## Build dependencies

This step creates a `requirements-lock.txt`

```bash
bazel run requirements.update
```

## Run `main`

```bash
bazel run //:main
```

## Run test

```bash
bazel test //src:test
```

## Run coverage (Writes nothing)

```bash
bazel coverage --combined_report=lcov //...
```
