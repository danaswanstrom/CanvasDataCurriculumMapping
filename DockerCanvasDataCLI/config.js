module.exports = {
  saveLocation: '/canvas_data/dataFiles',
  unpackLocation: '/canvas_data/unpackedFiles',
  stateFile: './state.json',
  apiUrl: 'https://api.inshosteddata.com/api',
  key: process.env.CD_API_KEY,
  secret: process.env.CD_API_SECRET
}
