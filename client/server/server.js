const express = require('express')
const path = require('path')
const logger = require('../build/lib/logger')
const project = require('../project.config')
const compress = require('compression')
const proxyMiddleWare = require("http-proxy-middleware")
const proxyPath = "http://127.0.0.1:5000"
const proxyOption = {target: proxyPath, changeOrigoin: true}
const app = express()
app.use(compress())

app.use(express.static(path.resolve(project.basePath, project.outDir)))

app.use("/api", proxyMiddleWare(proxyOption))

app.listen(8888, () => {
  logger.success('Server is running at http://localhost:8888')
})
