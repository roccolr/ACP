package manager;

import java.util.Hashtable;

import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.naming.Context;
import javax.jms.*;

public class Manager {
    public static void main(String [] argv){
        Hashtable <String, String> prop = new Hashtable<>();
        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        prop.put("topic.request", "request_topic");
        prop.put("topic.compra", "compra_topic");
        prop.put("topic.vendi", "vendi_topic");
        try{
            Context jndiContext = new InitialContext(prop);

            TopicConnectionFactory topicConnectionFactory = (TopicConnectionFactory) jndiContext.lookup("TopicConnectionFactory");
            Topic requestTopic = (Topic)jndiContext.lookup("request");
            Topic compraTopic = (Topic)jndiContext.lookup("compra");
            Topic vendiTopic = (Topic)jndiContext.lookup("vendi");

            TopicConnection conn = topicConnectionFactory.createTopicConnection();
            conn.start();
            TopicSession session = conn.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);

            //serve un listener che ascolta i messaggi su request

            TopicSubscriber requestSubscriber = session.createSubscriber(requestTopic);
            requestSubscriber.setMessageListener(new RequestListener(session, compraTopic, vendiTopic));

            Thread.sleep(60000);

            requestSubscriber.close();
            session.close();
            conn.close();

        }catch (NamingException e){
            e.printStackTrace();
        }catch(JMSException e){
            e.printStackTrace();
        }catch(InterruptedException e){
            e.printStackTrace();
        }
    }
}
