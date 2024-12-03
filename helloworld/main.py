# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import phoenix as px
from colors import green
from helloworld.greet.greeting import Greeter



def say_hello() -> None:
    greeting = Greeter().greet("Pantsbuild")
    client = px.Client()
    print(client)
    print(green(greeting))


if __name__ == "__main__":
    say_hello()
