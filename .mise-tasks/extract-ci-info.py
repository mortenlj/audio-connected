#!/usr/bin/env python
# [MISE] description="Extract CI info"
# [MISE] hide=true
import json
import os
import tomllib


def load_mise():
    """Load mise.toml"""
    root = os.getenv("MISE_CONFIG_ROOT")
    mise_path = os.path.join(root, "mise.toml")
    with open(mise_path, "rb") as fobj:
        return tomllib.load(fobj)


def output_ci_tasks(mise_config):
    ci_tasks = mise_config["tasks"]["ci"]["depends"]
    output = os.getenv("GITHUB_OUTPUT")
    line = f"ci-tasks={json.dumps(ci_tasks)}\n"
    if output:
        with open(output, "a") as fobj:
            fobj.write(line)
    else:
        print(f"Would write {line!r} to output")


def main():
    print("Extracting CI info")
    mise_config = load_mise()
    output_ci_tasks(mise_config)


if __name__ == "__main__":
    main()
