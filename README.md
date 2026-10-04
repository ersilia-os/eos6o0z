# Atomization energy of small molecules

Returns the atomization energy of a molecule, the energy binding its constituent atoms together, without running an electronic structure calculation. QM7 supplied the reference data: 7,165 molecules taken from GDB13, each limited to 23 atoms with heavy atoms restricted to carbon, sulphur, oxygen and nitrogen. A graph transformer pretrained on 10 million unlabelled molecules was fine-tuned to reproduce the computed values. Predictions apply only to molecules of comparable size and elemental composition.

This model was incorporated on 2022-07-19.Last packaged on 2026-03-10.

## Information
### Identifiers
- **Ersilia Identifier:** `eos6o0z`
- **Slug:** `grover-qm7`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `MoleculeNet`, `Chemical graph model`, `Quantum properties`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Atomization energy in kcal/mol, where more negative values indicate a more strongly bound molecule.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| u0_atom | float | high | Atomization energy in the unrelaxed geometry (U0) |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos6o0z](https://hub.docker.com/r/ersiliaos/eos6o0z)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6o0z.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6o0z.zip)

### Resource Consumption
- **Model Size (Mb):** `1417`
- **Environment Size (Mb):** `2405`
- **Image Size (Mb):** `6680.29`

**Computational Performance (seconds):**
- 10 inputs: `35.23`
- 100 inputs: `161.61`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/tencent-ailab/grover](https://github.com/tencent-ailab/grover)
- **Publication**: [https://doi.org/10.48550/arXiv.2007.02835](https://doi.org/10.48550/arXiv.2007.02835)
- **Publication Type:** `Preprint`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [Amna-28](https://github.com/Amna-28)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos6o0z
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos6o0z
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
