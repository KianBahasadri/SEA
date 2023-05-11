function checkEmailForCode(secretCode) {
  // Set up IMAP client
  const imap = new Imap({
    user: botEmailName,
    password: botEmailPassword,
    host: botEmailIMAP,
    port: 993,
    tls: true
  });

  imap.once('ready', () => {
    imap.openBox('INBOX', (err, box) => {
      if (err) throw err;

      // Search for emails 
      imap.search('ALL', (err, results) => {
        if (err) throw err;

        // Fetch the emails and check for secretCode in the subject
      const f = imap.fetch(results, { bodies: '' });
      f.on('message', (msg) => {
        let sender = '';
        let subject = '';
        msg.on('headers', (headers) => {
          // Extract the sender and subject from the email headers
          const parsedHeaders = mailparser.simpleParser(headers);
          sender = parsedHeaders.from.value[0].address;
          subject = parsedHeaders.subject;
        });
        msg.on('body', (stream, info) => {
          let buffer = '';
          stream.on('data', (chunk) => {
            buffer += chunk.toString('utf8');
          });
          stream.on('end', () => {
            // Check if the email subject contains the secret code
            if (subject.includes('secretCode')) {
              return sender;
            } else {
              return 'false';
            }
          });
        });
      });
      f.once('error', (err) => {
        throw err;
      });
      f.once('end', () => {
        imap.end();
      });
      });
    });
  });

  // Log any errors that occur during the connection process
  imap.once('error', (err) => {
    console.error(err);
  });

  // Log a message when the connection is closed
  imap.once('end', () => {
    console.log('Connection ended');
  });

  // Connect to the IMAP server
  imap.connect();
}

mode.exports = { checkEmailForCode };

