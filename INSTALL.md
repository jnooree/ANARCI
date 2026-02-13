# ANARCI INSTALLATION

- Create a conda environment using the provided environment.yml file:

  ```shell
  conda env create -f build_pipeline/environment.yml
  conda activate anarci-build
  ```

- Run the build pipeline to download germline data and build HMMs. During the
  build process, germline data will be downloaded from IMGT/GENE-DB and used to
  build hidden Markov models.

  ```shell
  build_pipeline/RUN_pipeline.sh
  ```

- Then install ANARCI using pip:

  ```shell
  pip install [-e] .
  ```

- For help see README or run:

  ```shell
  ANARCI -h
  ```
