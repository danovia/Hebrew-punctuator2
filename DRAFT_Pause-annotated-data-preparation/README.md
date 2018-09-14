# DRAFT - Training with pause annotated data

Training the model with pause-annotated texts improved it’s results for English in past researches, for example:
```to be ,COMMA or not to be ,COMMA that is the question .PERIOD```
* *(Optional)* Pause annotated text files for training and validation of the second phase model. These should be cleaned in the same way as the first phase data. Pause durations in seconds should be marked after each word with a special tag `<sil=0.200>`. Punctuation mark, if any, must come after the pause tag.

Example:
```to <sil=0.000> be <sil=0.100> ,COMMA or <sil=0.000> not <sil=0.000> to <sil=0.000> be <sil=0.150> ,COMMA that <sil=0.000> is <sil=0.000> the <sil=0.000> question <sil=1.000> .PERIOD```

We started parsing pause-annotated Hebrew texts to train the model, but we ran out of time. The task wasn’t trivial because the ASR system didn’t produce the right texts - when compared with the human transcripted text. We tried to adapt the ASR text with the human text, using [Synopsis Builder](https://synoptic.dicta.org.il/#), but we received bad results - many word gaps in both directions (human to ASR and ASR to human), what made the pause annotations unreliable without a heavy adaptation work.
*Within the limited time we didn’t finish this task and it remained as a draft.*

