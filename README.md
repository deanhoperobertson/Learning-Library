# Learning-Library
Collection of Jupyter notebook tutorials.

## Use this repo with repo2docker:
With two simple commands, you can be using this library interactively.
  1. `pip install jupyter-repo2docker`
  2. `jupyter-repo2docker https://github.com/James-Leslie/Learning-Library`

## Pull from DockerHub
Alternatively, you can pull and run a docker image for this repo directly using:   
`(sudo) docker run -it -p 8888:8888 jimbabwe/learning-library:latest`   

And to use persistent storage:
`(sudo) docker run -d -v ./1_Linear_Regression:/1_Linear_Regression -p 8888:8888 jimbabwe/learning-library:latest`
