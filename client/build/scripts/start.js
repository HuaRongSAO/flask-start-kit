const logger = require('../lib/logger')

logger.info('Starting server...')
require('../../server/main').listen(5555, () => {
  logger.success('Server is running at http://localhost:5555')
})
