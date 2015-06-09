'''
rpshttpserver.py - a web server example that runs inside Autodesk Revit

this example shows how to create an http REST API to Autodesk Revit.
'''

def main():
    contexts = ContextQueue()
    eventHandler = RpsEventHandler.Create(contexts)
    externalEvent = ExternalEvent.Create(eventHandler)
    server = RpsServer(externalEvent, contexts)
    serverThread = Thread(ThreadStart(server.serve_forever))
    serverThread.Start()


class ContextQueue(object):
    def __init__(self):
        from System.Collections.Concurrent import ConcurrentQueue
        self.contexts = ConcurrentQueue[HttpListenerContext]()

    def __len__(self):
        return len(self.contexts)

    def append(self, c):
        self.contexts.Enqueue(c)

    def pop(self):
        success, context = self.contexts.TryDequeue()
        if success:
            return context
        else:
            raise Exception("can't pop an empty ContextQueue!")


class RpsEventHandler(IExternalEventHandler):
    def __init__(self, contexts):
        self.contexts = contexts
        self.handlers = {
            'schedules': self.get_schedules
            # add other handlers here
        }

    def Execute(self, uiApplication):
        while self.contexts:
            context = self.contexts.pop()
            request = context.Request
            parts = request.RawUrl.split('/')
            handler = parts[0]  # FIXME: add error checking here!
            args = parts[1:]
            try:
                rc, ct, data = self.handlers[handler](args, uiApplication)
            except:
                rc = 404
                ct = 'text/plain'
                data = traceback.format_exc()
            response = context.Response
            response.ContentType = ct
            response.StatusCode = rc
            buffer = Encoding.UTF8.GetBytes(data)
            response.ContentLength64 = buffer.Length
            output = response.OutputStream
            output.Write(buffer, 0, buffer.Length)
            output.Close()

    def get_schedules(args, uiApplication):
        '''add code to get a specific schedule by name here'''

