from livereload import Server, shell

server = Server()
server.watch('src/**/*', shell('make build'))
server.serve(root='_build')