<template>
  <div>
    <h2>Insights Data</h2>
    <ul v-if="insights.length">
      <li v-for="item in insights" :key="item.PK">{{ item }}</li>
    </ul>
    <p v-else>No insights available.</p>
  </div>
</template>

<script>
import { gql, useQuery } from '@apollo/client/core'

const GET_INSIGHTS = gql`
  query {
    insights {
      PK
      SK
      # Add other fields as needed
    }
  }
`

export default {
  name: 'Insights',
  setup() {
    const { result, loading, error } = useQuery(GET_INSIGHTS)

    return {
      insights: result || [],
      loading,
      error
    }
  }
}
</script>