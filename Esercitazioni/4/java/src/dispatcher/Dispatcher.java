package dispatcher;

import java.util.Hashtable;

import javax.jms.*;
import javax.naming.*;


public class Dispatcher {
    public static void main(String [] argv){
        Hashtable <String, String> prop = new Hashtable<>();
        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        prop.put("queue.richiesta", "richiesta");
        // prop.put("queue.risposta", "risposta");

        try{
            ServerProxy proxy = new ServerProxy();
            Context jndiContext = new InitialContext(prop);
            QueueConnectionFactory queueConnectionFactory = (QueueConnectionFactory)jndiContext.lookup("QueueConnectionFactory");
            Queue queueRichiesta = (Queue)jndiContext.lookup("richiesta");

            QueueConnection queueConn = queueConnectionFactory.createQueueConnection();
            queueConn.start();
            QueueSession queueSession = queueConn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            QueueReceiver receiver = queueSession.createReceiver(queueRichiesta);
            receiver.setMessageListener(new RequestListener(queueSession, proxy));

            while(true){
                Thread.sleep(60000);
            }

        }catch(NamingException e){
            e.printStackTrace();
        }catch(JMSException e){
            e.printStackTrace();
        }catch (InterruptedException e){
            e.printStackTrace();
        }

    }
}
