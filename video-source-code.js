ifunction mailCleaner() {
  const file = SpreadsheetApp.openById('1ZP-6NU0rr2ITK33f3B6ksvB8NxHJPlk8DMJybBRcOJg')
  const sheet = file.getSheetByName('Sheet1')
  const range = sheet.getRange("A1:A4")
  const values = range.getValues()

  const filters = values.map(row => row[0])
  const searchQuery = filters.join(" OR ")

  console.log(searchQuery)
  const threads = GmailApp.search(searchQuery);
  const messagesProcessed = []

  threads.forEach(thread => {
    const messages = thread.getMessages()
    
    messages.forEach(msg => {
      const subject = msg.getSubject()
      messagesProcessed.push(subject)
    })
  })

  console.log(messagesProcessed)
  GmailApp.sendEmail("nomad@codingnomads.co", "summary", messagesProcessed.join(" "))
}
