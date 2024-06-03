load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "4912ced70dc1a2a8e4b86cec233b192ca053e82bc72d877b98e126156e8f228d",
    strip_prefix = "rules_python-0.32.2",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.32.2/rules_python-0.32.2.tar.gz",
)

load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_multi_toolchains")

py_repositories()

default_python_version = "3.11"

python_register_multi_toolchains(
    name = "python",
    default_version = default_python_version,
    python_versions = [
        "3.11",
        "3.10",
    ],
    register_coverage_tool = True,
)

load("@python//:pip.bzl", "multi_pip_parse")
load("@python//3.11:defs.bzl", interpreter_3_11 = "interpreter")
load("@python//3.10:defs.bzl", interpreter_3_10 = "interpreter")

multi_pip_parse(
    name = "pip_deps",
    default_version = default_python_version,
    python_interpreter_target = {
        "3.11": interpreter_3_11,
        "3.10": interpreter_3_10,
    },
    requirements_lock = {
        "3.11": "//py:requirements-lock.txt",
        "3.10": "//py:requirements-lock.txt",
    },
)

load("@pip_deps//:requirements.bzl", install_deps = "install_deps")

install_deps()
