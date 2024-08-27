# Project Moonshot Demo

### Installation and Prep

```bash
# Create env using conda
conda create -n moonshot python==3.11
conda activate moonshot

# Clone moonshot
git clone https://github.com/aiverify-foundation/moonshot.git
cd moonshot

# Install Project Moonshot's Python Library
pip install "aiverify-moonshot[all]"

# Clone and install test assets and Web UI (install node.js)
python -m moonshot -i moonshot-data -i moonshot-ui 

OR 

python -m moonshot -i moonshot-data # No UI

# Start CLI
python -m moonshot cli interactive
```

#### If you need to install NPM and Node.js for UI

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
nvm install 20
node -v # 20.11.1
npm -v # 10.8.1
```

#### How to port-forward from VM to local host using iptables

```bash
sudo iptables -L -v # Check the existing rules
sudo nano /etc/sysctl.conf # Enter the sysctl.conf file
  -> # Uncomment `net.ipv4.ip_forward=1` line
sudo sysctl -p # Apply changes

# Adding the IP tables rule
sudo iptables -t nat -A PREROUTING -p tcp --dport 4000 -j DNAT --to-destination 192.168.1.5:3000
sudo iptables -t nat -A POSTROUTING -p tcp -d 192.168.1.5 --dport 3000 -j MASQUERADE

# Save the rules
sudo apt-get install iptables-persistent
sudo netfilter-persistent save

# Check if the rules have been added in correctly
sudo iptables -t nat -L -v

# Go to http://172.31.74.219:4000/redteaming on local machine
```

### Other installation options
```bash
# To install Moonshot library APIs only
pip install aiverify-moonshot

# To install Moonshot's full functionalities (Library APIs, CLI and Web APIs)
pip install "aiverify-moonshot[all]"

# To install Moonshot library APIs and Web APIs only
pip install "aiverify-moonshot[web-api]"

# To install Moonshot library APIs and CLI only
pip install "aiverify-moonshot[cli]"

# To install from source code (Full functionalities)
git clone git@github.com:aiverify-foundation/moonshot.git
cd moonshot
pip install -r requirements.txt
```

### Install from source code
```bash
# Use this method if you are trying to pull from a specific branch of moonshot (e.g. branch that implements bug fixes). 

git clone -b ms-352_fix_CLI_ART_pt_id  git@github.com:aiverify-foundation/moonshot.git
cd moonshot
pip install -r requirements.txt
python -m moonshot -i moonshot-data
```


### Attack Modules
| Attack Modules | description |  
|---|---|   
| Charswap Attack |  This module tests for adversarial textual robustness. It creates perturbations through swapping characters for words that contains more than 3 characters.&lt;br&gt;Parameters:&lt;br&gt;1. MAX_ITERATIONS - Number of prompts that should be sent to the target. [Default: 10]&lt;br&gt;2. word_swap_ratio - Percentage of words in a prompt that should be perturbed. [Default: 0.2]&lt;br&gt; |  
| Colloquial Wordswap Attack | This attack module tests for textual robustness against the Singapore context. It takes in prompts that feature nouns that describe people. Examples of this include words like &#x27;girl&#x27; , &#x27;boy&#x27; or &#x27;grandmother&#x27;. The module substitutes these words with their Singapore colloquial counterparts, such as &#x27;ah boy&#x27;, &#x27;ah girl&#x27; and &#x27;ah ma&#x27;. |  
| Homoglyph Attack |  This module tests for adversarial textual robustness. Homoglyphs are alternative words for words comprising of ASCII characters.&lt;br&gt;Example of a homoglyph fool -&gt; fooI&lt;br&gt;This module purturbs the prompt with all available homoglyphs for each word present.&lt;br&gt;Parameters:&lt;br&gt;1. MAX_ITERATIONS - Maximum number of prompts that should be sent to the target. [Default: 20]. |  
| Insert Punctuation Attack |  This module tests for adversarial textual robustness and creates perturbations through adding punctuation to the start of words in a prompt.&lt;br&gt;Parameters:&lt;br&gt;1. MAX_ITERATIONS - Number of prompts that should be sent to the target. [Default: 10]&lt;br&gt;2. word_swap_ratio - Percentage of words in a prompt that should be perturbed. [Default: 0.2]. |  
| Job Role Generator | This attack module adds demographic groups to the job role. |  
| Malicious Question Generator | This attack module generates malicious questions using OpenAI&#x27;s GPT4 based on a given topic. This module will stop by the number of iterations (Default: 50). To use this attack module, you need to configure an &#x27;openai-gpt4&#x27;endpoint. |  
| Sample Attack Module | This is a sample attack module. |  
| Textfooler | This module tests for adversarial textual robustness and implements the perturbations listed in the paper Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment. &lt;br&gt;Parameters:&lt;br&gt;1. MAX_ITERATIONS - Number of prompts that should be sent to the target. This is also the number of transformations that should be generated. [Default: 5]&lt;br&gt;2. word_swap_ratio - Percentage of words in a prompt that should be perturbed. [Default: 0.2]&lt;br&gt;3. cosine_sim - Minimum word embedding cosine similarity [Default: 0.5]&lt;br&gt;4. window_size - Window size for the Universal Sentence Encoder (USE). [Default: 15]&lt;br&gt;5. threshold - Semantic similarity threshold for the USE. [Default: 0.840845057]&lt;br&gt;6. max_candidates - Number of nearest candidates to swap words with. [Default: 50]&lt;br&gt;Note:&lt;br&gt;Usage of this attack module requires the internet. Initial downloading of the GLoVe embedding occurs when the UniversalEncoder is called.&lt;br&gt;Embedding is retrieved from the following URL: https://textattack.s3.amazonaws.com/word_embeddings/paragramcf |  
| Textbugger | This module tests for adversarial textual robustness and implements the perturbations listed in the paper: TEXTBUGGER: Generating Adversarial Text Against Real-world Applications.\nParameters:\n1. MAX_ITERATIONS - Number of prompts that should be sent to the target. This is also the number of transformations that should be generated. [Default: 5]<br>2. word_swap_ratio - Percentage of words in a prompt that should be perturbed. [Default: 0.2]<br>3. top_k - To select top k number of semantic words from the GLoVe embedding. [Default: 5]<br>4. threshold - semantic similarity threshold for the universal encoder. [Default: 0.8]<br>Note:<br>Usage of this attack module requires the internet. Initial downloading of the GLoVe embedding occurs when the UniversalEncoder is called.\nEmbedding is retrieved from the following URL: https://textattack.s3.amazonaws.com/word_embeddings/paragramcf" |  
| Toxic Sentence Generator |  This module generates toxic sentence based on a given seed prompt. The attack module intends to test if the system under tests will complete the sentence with toxic sentences/phrases. | 
| Violent Durian | This is a multi-turn agent designed to interact over several exchanges. It&#x27;s used to elicit dangerous or violent suggestions from the target language model by adopting a criminal persona. The application is experimental and uses OpenAI GPT-4. Configure the endpoint openai-gpt4 to use this attack module. |  

## Connecting Endpoints
```bash
> list_endpoints # lists all endpoints
> update_endpoint -h # Will give you endpoint update format
```
### Update OpenAI Connectors
```bash
# Update Token for OpenAI GPT4
> update_endpoint openai-gpt4 "[('token', '')]"

# Update Token for OpenAI GPT 3.5
> update_endpoint openai-gpt35-turbo "[('token', '')]"

# Verify using list_endpoints
```
### Update Ollama Connectors + Install
```bash
sudo apt install curl # If not already installed
curl -fsSL https://ollama.com/install.sh | sh

# Test API
ollama pull llama3:8b
curl http://localhost:11434/api/generate -d '{
  "model": "mistral",
  "prompt": "Why is the sky blue?"
}'

# Assuming it works, update endpoint in moonshot CLI
cd moonshot-data/connectors-endpoints
nano ollama-llama3.json # update llama3 -> llama3:8b
```

#### Create new endpoint w/ Ollama
```bash
ollama pull [model name]:[parameters]

# Add endpoint (e.g. Ollama 3.1)
> add_endpoint openai-connector 'Ollama Llama3.1' http://localhost:11434/v1/ ollama 10 1 "{}"

# Update params list manually
cd moonshot-data/connectors-endpoints
ls # should display all .json files including llama 3.1
nano ollama-llama3-1.json # add params and save

> list_endpoints # should list Ollama 3.1
```

## Red Teaming

```bash
# List available sessions
> list_sessions

# Format for starting new session
> new_session -h

# Use an existing session
> use_session toxic-test-1

# Ending a session 
end_session
```

### Create new session

```bash
# Test toxic sentence attack module
> new_session toxic-test-1 -e "['openai-gpt4', 'openai-gpt35-turbo', 'ollama-llama3', 'ollama-llama3-1']" -p real-toxicity-prompt-template1
> new_session malicious-question-3 -e "['openai-gpt4', 'ollama-llama3', 'ollama-llama3-1', 'ollama-mistral', 'ollama-phi3', 'ollama-gemma2']"
# Session will start
> Hello! # Manual red-teaming

# Automated red teaming
> run_attack_module toxic_sentence_generator "What the hell" -p real-toxicity-prompt-template1
> run_attack_module malicious_question_generator "Computer Science"
```
