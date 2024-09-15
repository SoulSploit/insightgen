import Vue from 'vue'
import App from './App.vue'
import { ApolloClient, InMemoryCache, ApolloProvider } from '@apollo/client/core'

Vue.config.productionTip = false

const client = new ApolloClient({
  uri: process.env.VUE_APP_GRAPHQL_ENDPOINT,
  cache: new InMemoryCache()
})

new Vue({
  apolloProvider: new ApolloProvider({
    defaultClient: client
  }),
  render: h => h(App)
}).$mount('#app')
