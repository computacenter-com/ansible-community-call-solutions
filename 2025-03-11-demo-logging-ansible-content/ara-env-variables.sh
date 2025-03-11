printf "### Exporting environment variables for ARA API server. ###\n"
export ANSIBLE_CALLBACK_PLUGINS=$(python3 -m ara.setup.callback_plugins)
export ARA_API_CLIENT=http
export ARA_API_SERVER="http://127.0.0.1:8000"