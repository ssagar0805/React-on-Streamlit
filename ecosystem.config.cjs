module.exports = {
  apps: [
    {
      name: 'truthlens-streamlit',
      script: 'python',
      args: '-m streamlit run app_simple.py --server.port 3001 --server.address 0.0.0.0 --server.headless true',
      cwd: '/home/user/React-on-Streamlit',
      env: {
        NODE_ENV: 'production',
        PORT: 3001,
        STREAMLIT_BROWSER_GATHER_USAGE_STATS: 'false'
      },
      watch: false,
      instances: 1,
      exec_mode: 'fork',
      max_restarts: 3,
      restart_delay: 5000,
      log_file: 'streamlit.log',
      out_file: 'streamlit_out.log',
      error_file: 'streamlit_error.log'
    }
  ]
}