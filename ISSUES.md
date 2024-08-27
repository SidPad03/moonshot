## Issues and Resolutions

> ### Errors installing torch 2.3.0
```bash
ERROR: Ignored the following versions that require a different python version: 0.28.0 Requires-Python >=3.7, <3.11; 1.21.2 Requires-Python >=3.7,<3.11; 1.21.3 Requires-Python >=3.7,<3.11; 1.21.4 Requires-Python >=3.7,<3.11; 1.21.5 Requires-Python >=3.7,<3.11; 1.21.6 Requires-Python >=3.7,<3.11; 1.6.2 Requires-Python >=3.7,<3.10; 1.6.3 Requires-Python >=3.7,<3.10; 1.7.0 Requires-Python >=3.7,<3.10; 1.7.1 Requires-Python >=3.7,<3.10; 1.7.2 Requires-Python >=3.7,<3.11; 1.7.3 Requires-Python >=3.7,<3.11; 1.8.0 Requires-Python >=3.8,<3.11; 1.8.0rc1 Requires-Python >=3.8,<3.11; 1.8.0rc2 Requires-Python >=3.8,<3.11; 1.8.0rc3 Requires-Python >=3.8,<3.11; 1.8.0rc4 Requires-Python >=3.8,<3.11; 1.8.1 Requires-Python >=3.8,<3.11
ERROR: Could not find a version that satisfies the requirement torch==2.3.0 (from versions: 2.0.0, 2.0.1, 2.1.0, 2.1.1, 2.1.2, 2.2.0, 2.2.1, 2.2.2)
ERROR: No matching distribution found for torch==2.3.0

# Resolution: Install the latest version of torch compatible with x86 Intel MBP
pip install torch==2.2.2
```

> ### Errors when running automated-red-teaming using attack module
```bash
moonshot (test-runner-toxic) [PT: real-toxicity-prompt-template1, CS: ]> run_attack_module toxic_sentence_generator "What is "
2024-07-24 23:32:19,104 [INFO][runner.py::run_red_teaming(476)] [Runner] test-runner-toxic - Running red teaming session...
2024-07-24 23:32:19,106 [INFO][session.py::__init__(290)] [Session] Session already exists.
2024-07-24 23:32:19,137 [INFO][redteaming.py::generate(92)] [Red teaming] Starting automated red teaming...
2024-07-24 23:32:22.150418: I tensorflow/core/util/port.cc:113] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2024-07-24 23:32:22.246321: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 AVX512F AVX512_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2024-07-24 23:32:23.162084: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
2024-07-24 23:32:25,470 [INFO][redteaming.py::run_automated_red_teaming(161)] [Red teaming] Starting to run attack module [Toxic Sentence Generator]
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
2024-07-24 23:32:30,204 [INFO][connector.py::get_prediction(301)] Predicting prompt 1 [openai-gpt4]
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2024-07-24 23:32:38,460 [ERROR][session.py::run(453)] [Session] Failed to run runner processing module in Part 3 due to error: 1 validation error for RedTeamingPromptArguments
pt_id
  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
    For further information visit https://errors.pydantic.dev/2.7/v/string_type
[run_attack_module]: str(1 validation error for RedTeamingPromptArguments
pt_id
  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
    For further information visit https://errors.pydantic.dev/2.7/v/string_type)

# Resolution: Create ticket in Github related to pt_id issue.

Github Ticket: "https://github.com/aiverify-foundation/moonshot/issues/270"
Told to pull from "https://github.com/aiverify-foundation/moonshot/tree/ms-352_fix_CLI_ART_pt_id" to resolve this issue. Latest updates to project moonshot will resolve this issue. 
```

>  ### Runtime Error during buidling process of pylcs

```bash
PIC -I/home/vagrant/miniconda3/envs/moonshot/include/python3.11 -c /tmp/tmpzkoj946v.cpp -o tmp/tmpzkoj946v.o -std=c++11
      Traceback (most recent call last):
        File "/home/vagrant/miniconda3/envs/moonshot/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in <module>
          main()
        File "/home/vagrant/miniconda3/envs/moonshot/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/home/vagrant/miniconda3/envs/moonshot/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 251, in build_wheel
          return _build_backend().build_wheel(wheel_directory, config_settings,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/build_meta.py", line 415, in build_wheel
          return self._build_with_temp_dir(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/build_meta.py", line 397, in _build_with_temp_dir
          self.run_setup()
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/build_meta.py", line 313, in run_setup
          exec(code, locals())
        File "<string>", line 91, in <module>
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/__init__.py", line 108, in setup
          return distutils.core.setup(**attrs)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/_distutils/core.py", line 184, in setup
          return run_commands(dist)
                 ^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/_distutils/core.py", line 200, in run_commands
          dist.run_commands()
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 970, in run_commands
          self.run_command(cmd)
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/dist.py", line 945, in run_command
          super().run_command(command)
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 989, in run_command
          cmd_obj.run()
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/command/bdist_wheel.py", line 373, in run
          self.run_command("build")
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/_distutils/cmd.py", line 316, in run_command
          self.distribution.run_command(command)
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/dist.py", line 945, in run_command
          super().run_command(command)
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 989, in run_command
          cmd_obj.run()
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/_distutils/command/build.py", line 135, in run
          self.run_command(cmd_name)
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/_distutils/cmd.py", line 316, in run_command
          self.distribution.run_command(command)
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/dist.py", line 945, in run_command
          super().run_command(command)
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 989, in run_command
          cmd_obj.run()
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/command/build_ext.py", line 93, in run
          _build_ext.run(self)
        File "/tmp/pip-build-env-pr8b2irp/overlay/lib/python3.11/site-packages/setuptools/_distutils/command/build_ext.py", line 359, in run
          self.build_extensions()
        File "<string>", line 79, in build_extensions
        File "<string>", line 60, in cpp_flag
      RuntimeError: Unsupported compiler -- at least C++11 support is needed!
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for pylcs
  Building wheel for rouge-score (setup.py) ... done
  Created wheel for rouge-score: filename=rouge_score-0.1.2-py3-none-any.whl size=24934 sha256=7ebebbff674e8812630f8cf5c2a928fc64a488f6343ae1a1195db6b82d122292
  Stored in directory: /home/vagrant/.cache/pip/wheels/1e/19/43/8a442dc83660ca25e163e1bd1f89919284ab0d0c1475475148
  Building wheel for sqlitedict (setup.py) ... done
  Created wheel for sqlitedict: filename=sqlitedict-2.1.0-py3-none-any.whl size=16862 sha256=56e3ab23b5a8bc36c1d7cc54ded556f5fcbdc3ba9b62511df73f908c4a9898e8
  Stored in directory: /home/vagrant/.cache/pip/wheels/73/63/89/7210274f9b7fb033b8f22671f64c0e0b55083d30c3c046a3ff
  Building wheel for word2number (setup.py) ... done
  Created wheel for word2number: filename=word2number-1.1-py3-none-any.whl size=5566 sha256=b9086cd454b613204bac85a78e4d840b33d5524ac2c51676b15ac6a8d7005672
  Stored in directory: /home/vagrant/.cache/pip/wheels/cd/ef/ae/073b491b14d25e2efafcffca9e16b2ee6d114ec5c643ba4f06
Successfully built docopt gdown jieba langdetect mpld3 pinyin pptree rouge-score sqlitedict word2number
Failed to build pylcs
ERROR: Could not build wheels for pylcs, which is required to install pyproject.toml-based projects
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/home/vagrant/code/moonshot/moonshot/__main__.py", line 241, in <module>
    main()
  File "/home/vagrant/code/moonshot/moonshot/__main__.py", line 198, in main
    moonshot_data_installation()
  File "/home/vagrant/code/moonshot/moonshot/__main__.py", line 108, in moonshot_data_installation
    run_subprocess(["pip", "install", "-r", "requirements.txt"], check=True)
  File "/home/vagrant/code/moonshot/moonshot/__main__.py", line 28, in run_subprocess
    return subprocess.run(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vagrant/miniconda3/envs/moonshot/lib/python3.11/subprocess.py", line 569, in run
    raise CalledProcessError(retcode, process.args,

# Resolution (update compiler)
sudo apt-get update
sudo apt-get install g++-9
export CXX=g++-9
export CC=gcc-9
```