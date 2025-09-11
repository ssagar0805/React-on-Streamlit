module.exports = {
  apps: [
    {
      name: 'react-streamlit-app',
      script: 'python',
      args: '-m streamlit run app_simple.py --server.port 3001 --server.address 0.0.0.0 --server.headless true --browser.gatherUsageStats false',
      cwd: '/home/user/React-on-Streamlit',
      env: {
        STREAMLIT_BROWSER_GATHER_USAGE_STATS: 'false',
        STREAMLIT_SERVER_HEADLESS: 'true'
      },
      watch: false,
      instances: 1,
      exec_mode: 'fork'
    }
  ]
}