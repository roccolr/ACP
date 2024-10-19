package dispatcher;

import javax.jms.*;

public class myListener implements MessageListener {
    QueueConnection conn;

    public myListener(QueueConnection conn){
        this.conn = conn;
    }
    @Override
    public void onMessage(Message msg){
        TextMessage txt = (TextMessage)msg;
        
        DispatcherThread worker = new DispatcherThread(txt, conn);
        worker.start();
    }
}
