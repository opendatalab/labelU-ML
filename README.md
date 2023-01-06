# Introduction
## Quickstart


1. Setup environment
    
    ```bash
    conda create -n labelu-ml python=3.7
    conda activate labelu-ml
    ```
   
2. Install labelu-ml
   ```bash
   pip install labelu-ml
   ```

3. Initialize an ML application based on an example path:
   ```bash
   labelu-ml init my_ml_app --path labelu_ml/examples/the_simplest_app

   pip install -r my_ml_app/requirements.txt
   ```

4. Start ML application server
   ```bash
   labelu-ml start my_ml_app
   ```

## Usage

### Command line
```
$ labelu-ml --help
                                                                                                                                                     
 Usage: labelu-ml [OPTIONS] COMMAND [ARGS]...                                                                                                        
                                                                                                                                                     
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                           │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                                    │
│ --help                        Show this message and exit.                                                                                         │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ init                  Initailize an ML app from a example.                                                                                        │
│ start                 Start ML app server.                                                                                                        │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```