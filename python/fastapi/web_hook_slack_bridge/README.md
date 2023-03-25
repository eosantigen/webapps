# WebHook Slack Bridge

This is a small and very basic implementation that receives a JSON payload via POST and passes it customized onto Slack. This is due to the fact that the webhook payloads of some apps do not support the Slack API, which requires the payload to be sent within the field "text".