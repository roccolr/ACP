package dispatcher;
import java.util.Hashtable;

import javax.jms.*;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;


public class Dispatcher {
    public static void main(String[] args) {
        //impostiamo il lookup su JNDI di apache

        Hashtable <String, String> prop = new Hashtable<>();
        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        prop.put("queue.richiesta", "richiesta");
        prop.put("queue.risposta", "risposta");

        try{
            Context jndiContext = new InitialContext(prop);
            
            //otteniamo gli administered objects
            QueueConnectionFactory queueConnectionFactory = (QueueConnectionFactory)jndiContext.lookup("QueueConnectionFactory");
            Queue queueRichiesta = (Queue)jndiContext.lookup("richiesta");
            
            QueueConnection conn = queueConnectionFactory.createQueueConnection();

            conn.start();
            QueueSession session = conn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            
            QueueReceiver receiver = session.createReceiver(queueRichiesta);
            receiver.setMessageListener(new myListener(conn));
            
            while(true){
                Thread.sleep(100);
            }

        }catch(JMSException e){
            e.printStackTrace();
        }catch(NamingException e){
            e.printStackTrace();
        }catch(InterruptedException e){
            e.printStackTrace();
        }
    }
}
