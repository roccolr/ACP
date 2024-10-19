package def;

import javax.jms.*;
import javax.naming.*;
import java.util.Hashtable;


public class Sender {
    public static void main(String argv[]){
        Hashtable <String, String> prop = new Hashtable<>();

        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        prop.put("queue.test", "mytestqueue");
        try{
            Context jndiContext = new InitialContext(prop);

            //ottenimento degli administred objects
            QueueConnectionFactory queueConnFactory = (QueueConnectionFactory)jndiContext.lookup("QueueConnectionFactory");
            Queue queue = (Queue)jndiContext.lookup("test");

            QueueConnection queueConn = queueConnFactory.createQueueConnection();

            QueueSession session = (QueueSession)queueConn.createSession(false, Session.AUTO_ACKNOWLEDGE);

            // QueueReceiver receiver = session.createReceiver(queue);
            QueueSender sender = session.createSender(queue);

            TextMessage msg = session.createTextMessage();

            for(int i=0; i<5; i++){
                msg.setText("Hello_"+i);
                sender.send(msg);
            }
            msg.setText("fine");
            sender.send(msg);

            System.out.println ("I messaggi sono stati inviati!");
            
            sender.close();
            session.close();
            queueConn.close();

        }catch (Exception e){
            e.printStackTrace();
        }
    }    
}
