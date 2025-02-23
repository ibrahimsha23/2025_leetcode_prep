package com.example.urlshortener.service;

import com.example.urlshortener.model.Url;
import com.example.urlshortener.model.UrlDto;
import org.springframework.stereotype.Service;

@Service
public interface UrlService {
    public Url generateShortLink(UrlDto UrlDto);
    public Url persistShortLink(Url url);
    public Url getEncodedUrl(String url);
    public void deleteShortLink(Url url);

}
