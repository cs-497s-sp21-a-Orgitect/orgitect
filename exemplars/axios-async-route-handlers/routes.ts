import type {Request, Response} from "express"
import axios from 'axios'

export async function externalGetTest (req: Request, res: Response): Promise<void> {
    const externalResponse = await axios.get(`https://reddit.com/r/${req.query.subreddit}/top/.json`, {
        params: {
            t: req.query.time
        }
    })
    res.status(200).json(externalResponse.data.data)
}

export async function externalPostTest (req: Request, res: Response): Promise<void> {
    const externalResponse = await axios.post(`https://example.com/upload`, req.body)
    res.status(201).json(externalResponse.data.myContent)
}
