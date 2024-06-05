load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")


http_archive(
    name = "aspect_rules_py",
    sha256 = "959b433fa19238d3d3644be2960c606cea27b83a9ea8a0f1f7bd6d3be4fc53e9",
    strip_prefix = "rules_py-0.7.2",
    url = "https://github.com/aspect-build/rules_py/releases/download/v0.7.2/rules_py-v0.7.2.tar.gz",
)

load("@aspect_rules_py//py:repositories.bzl", "rules_py_dependencies")

rules_py_dependencies()

load("@aspect_rules_py//py:toolchains.bzl", "rules_py_toolchains")

rules_py_toolchains()


load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_toolchains")

python_register_toolchains(
    name = "python_3_10",
    python_version = "3.10",
    register_coverage_tool = True,
)

py_repositories()

load("@python_3_10//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "pip_deps",
    python_interpreter_target = interpreter,
    requirements_lock = "//py:requirements-lock.txt",
)

load("@pip_deps//:requirements.bzl", install_pypi_deps = "install_deps")

install_pypi_deps()
