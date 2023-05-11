const Imap = require('imap');
const { simpleParser} = require('mailparser');
const { SlashCommandBuilder } = require('discord.js');
const { botEmailName, botEmailPassword, botEmailIMAP } = require('../../config.json');
const { checkEmailForCode } = require("../../checkEmailForCode.js");
const { addRoles } = require("../../addRoles.js");
const VerificationChannel = "verification"

module.exports = {
	data: new SlashCommandBuilder()
		.setName('verify')
		.setDescription('Verify yourself and automatically assign roles'),
	async execute(interaction) {
		if (interaction.channel.name != VerificationChannel) return;

		let secretCode = Math.floor(Math.random() * 9000) + 1000;
		await interaction.reply({ content: `Please use your university email address to send the secretCode **${secretCode}** to the email address: **${botEmailName}**. (The email that is next to your name on the OnQ classlist.)`, ephemeral: true });
		
		let sender = "false";
		for (let i = 0; i < 60; i++) {
			sender = checkEmailForCode(secretCode);
			if (sender != "false") break;
		}

		if (sender == "false") {
			await interaction.editReply('Verification Timed Out.');
		} else {
			await interaction.editReply("Verification Successfully Completed!");
			addRoles(interaction.user.name, emailaddress);
		}
	},
};

