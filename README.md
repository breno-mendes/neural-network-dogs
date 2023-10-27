# Projeto Final - Modelos Preditivos Conexionistas

### Grupo

-   Breno Araújo
-   Filipe Pontes

| **Tipo de Projeto**      | **Modelo Selecionado** | **Linguagem** |
| ------------------------ | ---------------------- | ------------- |
| Classificação de Imagens | ResNet34               | PyTorch       |

## Performance

O modelo treinado possui performance de **100%**.

### Output do bloco de treinamento

<details>
  <summary>Click to expand!</summary>
  
  ```text
    Epoch 0/9
    ----------
    train Loss: 1.1817 Acc: 0.5333
    val Loss: 0.2135 Acc: 0.9600
    Epoch 1/9
    ----------
    train Loss: 0.5962 Acc: 0.8167
    val Loss: 0.0919 Acc: 0.9733
    Epoch 2/9
    ----------
    train Loss: 0.4614 Acc: 0.8600
    val Loss: 0.0674 Acc: 0.9733
    Epoch 3/9
    ----------
    train Loss: 0.5950 Acc: 0.7900
    val Loss: 0.0596 Acc: 0.9733
    Epoch 4/9
    ----------
    train Loss: 0.4398 Acc: 0.8600
    val Loss: 0.0371 Acc: 1.0000
    Epoch 5/9
    ----------
    train Loss: 0.3309 Acc: 0.9133
    val Loss: 0.0367 Acc: 1.0000
    Epoch 6/9
    ----------
    train Loss: 0.4004 Acc: 0.8733
    val Loss: 0.0256 Acc: 1.0000
    Epoch 7/9
    ----------
    train Loss: 0.3629 Acc: 0.8700
    val Loss: 0.0646 Acc: 0.9867
    Epoch 8/9
    ----------
    train Loss: 0.4021 Acc: 0.8767
    val Loss: 0.0404 Acc: 0.9867
    Epoch 9/9
    ----------
    train Loss: 0.3363 Acc: 0.8933
    val Loss: 0.0477 Acc: 0.9867
    Training complete in 16m 22s
    Melhor Acurácia: 1.0000
    Loss: 0.0120
    F1-Score: 1.0000
    Recall: 1.0000
    Precisão: 1.0000
  ```
</details>

### Evidências do treinamento

![Training and Validation Loss/Accuracy](https://github.com/breno-mendes/neural-network-dogs/blob/master/assets/Model%20Fixed%20Feature.png?raw=true)
![Matriz Confusão](https://github.com/breno-mendes/neural-network-dogs/blob/master/assets/Matriz%20de%20Confusao.png?raw=true)

## Roboflow

Dataset no Roboflow: [Raças de Cachorros](https://universe.roboflow.com/breno-03sky/racas-de-cachorros)

## HuggingFace

Modelo no HuggingFace: [Dog Breed Classification Model using ResNet34](https://huggingface.co/brenomendes/dog-breeds/blob/main/Dog_Breed_Classification_Model_using_ResNet34.ipynb)
