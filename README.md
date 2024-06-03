# bazel_learn

Repo for learning bazel with python.

## Build dependencies

This step creates a `requirements-lock.txt`

```bash
bazel run //py:requirements.update
```

## Run `main`

```bash
bazel run //src:main
```

## Run test

```bash
bazel test //src:name_test
```

## Run coverage

```bash
bazel coverage --combined_report=lcov //...
```
