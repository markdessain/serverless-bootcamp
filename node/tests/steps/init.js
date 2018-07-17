const { promisify } = require('util')
const awscred = require('awscred')
const AWS = require('aws-sdk')

let initialized = false

const init = async () => {
  if (initialized) {
    return
  }

  process.env.restaurants_api      = "https://4qkmw6oovb.execute-api.eu-west-1.amazonaws.com/dev/restaurants"
  process.env.restaurants_table    = "restaurants"
  process.env.AWS_REGION           = "eu-west-1"
  process.env.cognito_user_pool_id = "eu-west-1_z9AyExIfw"
  process.env.cognito_client_id    = "29oc5lf4tonbodmuhom07b1srm"

  const { credentials } = await promisify(awscred.load)({profile: 'serverless_personal'})

  process.env.AWS_ACCESS_KEY_ID     = credentials.accessKeyId
  process.env.AWS_SECRET_ACCESS_KEY = credentials.secretAccessKey

  console.log('AWS credential loaded')

  initialized = true
}

module.exports = {
  init
}
