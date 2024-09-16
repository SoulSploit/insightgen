module.exports = {
  devServer: {
    // Proxy configuration to forward requests to the backend server
    proxy: {
      '/api': {
        target: 'http://localhost:3000', // Adjust this if your backend server is running on a different port
        changeOrigin: true, // Change the origin header to match the target URL
        secure: false, // Set to true if the backend server uses HTTPS
        logLevel: 'debug' // Optional: useful for detailed proxy debugging
      }
    },
    // Server settings
    port: 8080, // Port for the development server
    open: true, // Open the browser automatically when the server starts
    historyApiFallback: true // Handle HTML5 History API fallback for single-page applications
  }
};
