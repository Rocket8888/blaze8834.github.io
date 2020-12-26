const Discord = require('discord.js')
const client = new discord.Client()
const config = require('./config.json')

client.on('ready' , () => {
  console.log('Client is ready!')
})

client.login(config.token)
