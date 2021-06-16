#git clone --depth=1 https://github.com/twintproject/twint.git
#cd twint
#pip install . -r requirements.txt
#pip uninstall dataclasses -y

import twint

# Configure
c = twint.Config()
c.Username = "joebiden"
c.Search = "milestone"

# Run
twint.run.Search(c)