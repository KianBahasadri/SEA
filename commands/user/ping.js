// Import the SlashCommandBuilder class from discord.js
const { SlashCommandBuilder } = require('discord.js');

// Export an object containing data about the command
module.exports = {
  // Use a new instance of SlashCommandBuilder to define the command
  data: new SlashCommandBuilder()
    .setName('ping') // Set the command name to "ping"
    .setDescription('Replies with Pong!'), // Set the command description

  // Define an async function to handle the command's execution
  async execute(interaction) {
    await interaction.reply('Pong!'); // Reply to the interaction with "Pong!"
  },
};

