package def;

import javax.jms.*;
import javax.naming.*;
import java.util.Hashtable;

public class Receiver {
    public static void main(String argv[]){
        Hashtable<String, String> prop = new Hashtable<String, String>();

        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        //		jndi queue name   queue-name
		prop.put( "queue.test", "mytestqueue" );

        try{
            Context jndiContext = new InitialContext(prop);

            //Lookup degli administrative objects

            //Connection ~ lookup ritorna object quindi va effettuato un cast
            QueueConnectionFactory queueConnFactory = (QueueConnectionFactory)jndiContext.lookup("QueueConnectionFactory");
            
            //Destination ~ a lookup() va passato il nome senza queue.
            Queue queue = (Queue)jndiContext.lookup("test");

            QueueConnection queueConn = queueConnFactory.createQueueConnection();

            //essendo Receiver, la connessione va avviata
            queueConn.start();

            //otteniamo la sessione
            QueueSession session = queueConn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            QueueReceiver receiver = session.createReceiver(queue);
            TextMessage message;
            do{
                System.out.println("[RECEIVER]\tIn attesa di messaggi...");
                message = (TextMessage)receiver.receive();
                System.out.println("[RECEIVER]\tMessaggio ricevuto: "+message.getText());                
            }while(!(message.getText().equals("fine")));

            receiver.close();
            session.close();
            queueConn.close();

        }catch (Exception e){
            e.printStackTrace();
        }


    }
}
