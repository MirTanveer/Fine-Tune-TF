
##  Important Notes

- For easy setup of a conda environment to run the notebooks, you can use the provided **`finetune.yml`** file in this folder.  
- Check [here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) for instructions on setting up an environment from a `.yml` file.  
- For detailed examples, refer to the information inside the notebooks.

---

###  Available Notebooks

| Notebook | Description | Colab Link |
|-----------|--------------|-------------|
| **Fine_Tuning_per_protein** | Predictions on protein level (classification) using full fine-tuned model | [Open in Colab](https://colab.research.google.com/drive/1yxnZiZ3aHmXc40fpR-ynPmT1u71geLnR?usp=sharing) |
| **Fine_Tuning_per_protein_with_LoRA** | Predictions on protein level (classification) with LoRA | [Open in Colab](https://drive.google.com/file/d/1KMcWfjuom2_oik8GykA9G1h6zdjeMoIM/view?usp=sharing) |
| **Inference_using_LoRA_650M_model** | Run inference on the TF test dataset using the trained LoRA-ESM2-650M model | [Open in Colab](https://colab.research.google.com/drive/1uENLqKBdOZihkczWLDzjdINxwZBYuCaL?usp=sharing) |

---

###  Supported Pretrained PLMs

| Model | Hugging Face Checkpoint |
|--------|--------------------------|
| **ESM2 8M** | `facebook/esm2_t6_8M_UR50D` |
| **ESM2 35M** | `facebook/esm2_t12_35M_UR50D` |
| **ESM2 150M** | `facebook/esm2_t30_150M_UR50D` |
| **ESM2 650M** | `facebook/esm2_t33_650M_UR50D` |
| **ESM2 3B** | `facebook/esm2_t36_3B_UR50D` |
| **Prot Bert** | `Rostlab/prot_bert` |


---

###  Parameter-Efficient Fine-Tuning (PEFT)

- PEFT is utilized through **[Hugging Face PEFT](https://github.com/huggingface/peft)**.  
- **LoRA** fine-tuning of different ESM2 variants is done with varied settings.  
- Optionally, full model fine-tuning can be performed (recommended for models smaller than *ESM2 3B*).  
- Other adapters from Hugging Face PEFT can be easily integrated.

---

###  Memory Efficiency Tips

- Always enable **mixed precision training**.  
- If GPU memory overflows:
  1. Reduce the batch size to 1 and simulate larger batches using **gradient accumulation**.     

---

###  Citation

If you use these notebooks in your research, please cite our work.

---

###  License

- **Data:** Released under the terms of the [CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/).  
- **Source Code:** Licensed under the [MIT License](./MIT-LICENSE.txt).

---

