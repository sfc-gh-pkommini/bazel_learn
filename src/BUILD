load("@rules_python//python:defs.bzl", "py_binary", "py_test", "py_library")
load("@pip_deps//:requirements.bzl", "requirement")

py_library(
    name = "name",
    srcs = [
      "name.py",
    ],
    deps = [
      requirement("requests"),
    ],
)

py_binary(
  name = "main",
  srcs = [
    "main.py",
  ],
  main = "main.py",
  deps = [
    ":name",
  ],
)

py_test(
    name = "name_test",
    srcs = ["name_test.py"],
    deps = [":name"],
)
